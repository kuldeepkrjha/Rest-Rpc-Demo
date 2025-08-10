import grpc
from concurrent import futures
from service_pb2 import UserResponse
import service_pb2_grpc

class UserService(service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        users = {
            "1": ("Windows User", "user@windows.com"),
            "2": ("Admin", "admin@windows.com")
        }
        name, email = users.get(request.user_id, ("Unknown", "N/A"))
        return UserResponse(
            user_id=request.user_id,
            name=name,
            email=email
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()