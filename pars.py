import requests
from bs4 import BeautifulSoup

rl = "https://www.newegg.com/Gaming-Laptops/SubCategory/ID-3365?Tid=167748"
page = requests.get(rl)
soup = BeautifulSoup(page.text, 'html.parser')

# 1 ვეძებთ სასურველი ფასის ან უფრო იაფ ლეპტოპებს
pricerange = soup.find_all(text="$")


def commaremove(str):
    restr = ''
    for x in str:
        if x == ",":
            pass
        else:
            restr += x
    return restr


def gpupricing(desiredprice):
    indx = 0
    prices = []
    for price in pricerange:
        parent = pricerange[indx].parent  # vigebt romeli HTML tag aris parent
        # radgan "$" <strong>$</strong> formit gvxvdeba, parentshi unda vipovot strong tagi
        strongtag = parent.find("strong")
        prices.append(int(commaremove(strongtag.string)))
        indx += 1
    acceptable = []
    for price in prices:
        if price <= desiredprice:
            acceptable.append(price)
    return acceptable


# daabrunebs masivs romelic sheicavs yvela 1500is an naklebi dolaris fasis mqone leptops
print(gpupricing(1500))
print(gpupricing(750))  # igive 750$ze


# 2 სპეციფიური ბრენდის ძებნა ლეპტოპებში
brandThisMuch = soup.find_all("a", class_="item-title")
allLaptops = []
indice = 0
for tag in brandThisMuch:
    allLaptops.append(brandThisMuch[indice].string)
    indice += 1
eligableBrands = ["Lenovo", "ASUS", "MSI"]


def brandSearch(brand):
    brandedLaptops = []
    for laptop in allLaptops:
        name = ''
        for i in laptop:
            if i != " ":
                name += i
            else:
                break
        if name == brand:
            brandedLaptops.append("---"+laptop+"---")
    return brandedLaptops


print(brandSearch(eligableBrands[0]))  # გამოიტანს Lenovo-ს ლეპტობების ცხრილს
print(brandSearch(eligableBrands[1]))  # გამოიტანს ASUS-ს ლეპტობების ცხრილს
print(brandSearch(eligableBrands[2]))  # გამოიტანს MSI-ს ლეპტობების ცხრილს
# 3 აქციაში მყოფი პროდუქციის ოდენობა
sales = soup.find_all("span", class_="price-save-percent")
salerroy = []
num = 0
for sale in sales:
    salerroy.append("Save :"+" "+sale.string)
    num += 1
print(salerroy, "Total items on sale :"+" "+str(num))
