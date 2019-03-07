import requests

#   Unknown YOR List:
#   6385 bytes


def getImageFileSize(link):
    imgLink = requests.get(link).text
    # print(len(imgLink))
    return len(imgLink)
    # print(f"Image size: {len()/1024} bytes")


# link = "http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltcAY4XCvAsCF3sVnd0AZTuIa3UIaPtd8T6dut6COn*Cfd1MRXDif4HLbAn7SV8AYYqAS.AV8tch3XsMOGuCRUB&time=201902151020&inya=true"
# print(getImageFileSize(link))
