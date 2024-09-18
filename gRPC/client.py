import grpc
import greeter_pb2
import greeter_pb2_grpc

def run():
    # Establecemos una conexión con el servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        # Llamamos al método SayHello del servidor
        response = stub.SayHello(greeter_pb2.HelloRequest(name='Juan'))
    print("Greeting:", response.message)

if __name__ == '__main__':
    run()