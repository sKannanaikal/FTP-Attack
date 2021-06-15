import ftplib
import optparse

def loginWithAnonymous(host):
    try:
        connection = ftplib.FTP(host)
        connection.login('Anonymous','yolo@gmail.com')
        print("[+] Connection Successful.  Host is Vulnerable to Anonymous FTP Logins!")
        connection.quit()
        return True

    except e:
        print("[-] Connection Not Possible via Anonymous Login")
        return False

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
