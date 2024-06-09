import socket
import threading

bank_accounts = {
    "123456": {"pin": "1234", "balance": 7700},
    "654321": {"pin": "4321", "balance": 1783}
}


def handle_client_connection(client_socket):
    try:
        client_socket.send("Enter your account number: ".encode())
        account_number = client_socket.recv(1024).decode().strip()

        if account_number in bank_accounts:
            client_socket.send("Enter your PIN: ".encode())
            pin = client_socket.recv(1024).decode().strip()

            if pin == bank_accounts[account_number]["pin"]:
                client_socket.send("Authentication successful!\n".encode())
                while True:
                    client_socket.send("Choose an option: 1. Check Balance 2. Deposit 3. Withdraw 4. Exit\n".encode())
                    option = client_socket.recv(1024).decode().strip()

                    if option == '1':
                        balance = bank_accounts[account_number]["balance"]
                        client_socket.send(f"Your balance is: ${balance}\n".encode())
                    elif option == '2':
                        client_socket.send("Enter amount to deposit: ".encode())
                        try:
                            amount = int(client_socket.recv(1024).decode().strip())
                            bank_accounts[account_number]["balance"] += amount
                            client_socket.send("Deposit successful!\n".encode())
                        except ValueError:
                            client_socket.send("Invalid amount entered. Try again.\n".encode())
                    elif option == '3':
                        client_socket.send("Enter amount to withdraw: ".encode())
                        try:
                            amount = int(client_socket.recv(1024).decode().strip())
                            if amount <= bank_accounts[account_number]["balance"]:
                                bank_accounts[account_number]["balance"] -= amount
                                client_socket.send("Withdrawal successful!\n".encode())
                            else:
                                client_socket.send("Insufficient funds!\n".encode())
                        except ValueError:
                            client_socket.send("Invalid amount entered. Try again.\n".encode())
                    elif option == '4':
                        final_balance = bank_accounts[account_number]["balance"]
                        client_socket.send(f"Your final balance is: ${final_balance}\n".encode())
                        break
                    else:
                        client_socket.send("Invalid option. Please choose again.\n".encode())
            else:
                client_socket.send("Authentication failed. Incorrect PIN.\n".encode())
        else:
            client_socket.send("Authentication failed. Account not found.\n".encode())
    finally:
        client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server is running on port 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"New connection from {addr}")
        client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    main()
