import grpc
from concurrent import futures
import time

# Importamos los archivos generados
import greeter_pb2
import greeter_pb2_grpc

# Implementación del servicio
class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        response = greeter_pb2.HelloResponse()
        response.message = f'Hello, {request.name}!'
        return response

# Crear el servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor iniciado en el puerto 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()