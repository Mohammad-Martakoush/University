import socket


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 9999))

        while True:
            response = client.recv(4096).decode()
            print(response)

            if "Enter" in response or "Choose" in response or "Try" in response:
                client_input = input()
                client.send(client_input.encode())

            if "Your final balance is" in response:
                break

    except socket.error as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
