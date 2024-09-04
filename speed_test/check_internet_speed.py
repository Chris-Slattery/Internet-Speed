import speedtest


def check_internet_speed():

    #create an object for speedtest
    st = speedtest.Speedtest()


    #Find the best server base on ping rate
    st.get_best_server()


    #Perform download and upload speed tests and convert to Mbps
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000

    #Test ping rate
    ping = st.results.ping

    #Show results
    print(f"Download Speed is: {download_speed:.2f} Mbps")
    print(f"Upload Speed is: {upload_speed:.2f} Mbps")
    print(f"Ping is: {ping:.2f} ms")


if __name__ == "__main__":
    check_internet_speed()