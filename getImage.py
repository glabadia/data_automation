from time import sleep
import requests
from bs4 import BeautifulSoup as Soup

# url='https://en.wikipedia.org/wiki/Agent_Orange'
# url = 'http://img2.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltAYXIsYFSKhOGuLuTuIa3UIaPtIuTwIa3X7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tQ46XsMOGuhK&time=201902131250&inya=true'
# url = 'http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltAYXIs8FGl48TuIa3UIaPtIuTXIaYw7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201902131520&inya=true'


# html = Soup(requests.get(url).text, features="lxml")
# html = requests.get(url, stream=True)
# html = requests.get(url)
# data = html.text
# print(f"Image size: {len(data)} bytes")

# image_links = [(url + a['href'])
#                for a in html.find_all('a', {'class': 'image'})]

# for img_url in image_links:
#     response = requests.get(img_url)
#     try:
#         print(
#             f"Size of image {img_url} = {response.headers['Content-Length']} bytes")
#     except KeyError:
#         print(f"Server didn't specify content length in headers for {img_url}")
#     sleep(0.5)


urlList = [
    "http://138.201.52.234/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtDrHbHJEvczM",
    "http://138.201.52.236/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtEeQNQigrh7z",
    "http://138.201.52.234/imgs/dyJ2O5ZGYxX3QVFVucXdYkUoGQvH3jVfVM7DukZlTg",
    "http://img1.jcarinfo.net/gixlarge.php?&op=CRKqIaIKIagKIltNg5IqcltcAYS076UHh53sImetWQe*Ia1sIQeUIut6COn*Cfd1MRXDif4HLbAn7SV8AYYqV1SIY6Yq8B0dLvVsh5nr4K&time=201903082320",
    "http://img3.jcarinfo.net/gix.php?&amp;op=4BIqIaIKIagKIltNg5IqcltcAYS076UHh53sImetWQe*Ia1sIQeXI8t6COn*Cfd1MRXDif4HLbAn7SV8AYYqV1SIY6Yq8B0dLvVsh5nr4K&amp;time=201903082340",
    "http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5Iqclta2Y3s25SU7*PKIQ1KI*3*7*kKIaY*7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201903131640&inya=true",
    "http://img1.jcarinfo.net/gix.php?&op=hvIqIaIKIagKIltNg5Iqclta2Y3s25SU7*PKIQ1KI*3*7*kKIaY*7bVJCfdNhFVXLRXUM5SqMRYqAS.AV8tO2YtQV8tch3XsMOGuCRUB&time=201903131640",
    "http://138.201.52.234/imgs/9I3PnMMQPlsKJY7SMtAJoQUpPupIhJUjEujYykXmoxWDoAi-ETxGBvgdwmvSwT-7",
    "http://img1.jcarinfo.net/gix.php?&op=ifPqIaIKIagKIltNg5IqcltcAYS076n*COnpgfMH7*PKIQ1KI*3*7*3KIQeqMOHNhFn*4bADLfnFgRtX48tYYnAS7340QSdS7S0uL6NHhOSr&time=20190313170&inya=true"
]
# url = "http://138.201.52.234/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtDrHbHJEvczM"
# url = "http://138.201.52.236/imgs/dyJ2O5ZnVGaLpjCgSr4JtiXYvulKsUtEeQNQigrh7z"
# url = "http://138.201.52.234/imgs/dyJ2O5ZGYxX3QVFVucXdYkUoGQvH3jVfVM7DukZlTg"


def getImageFileSize(link):
    import requests
    imgLink = requests.get(link).text
    return len(imgLink)


for url in urlList:
    print(getImageFileSize(url))


def sample_function(x=433):
    # if 900 > x > 15:
    #     print("true")
    # else:
    #     print("false")
    return 900 > x > 15


print(sample_function())
