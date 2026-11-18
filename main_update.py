def observe(store):
    for dep, sections in store.items():
        print(dep)
        for sec, items in sections.items():
            print("  ", sec, items)


def add(store):
    x = input("1. item  2. section: ")
    dep = input("department: ")
    if x == "1":
        sec = input("section: ")
        name = input("item: ")
        store[dep][sec][name] = input("price: ")
    else:
        store[dep][input("new section: ")] = {}


def remove(store):
    x = input("1. item  2. section: ")
    dep = input("department: ")
    sec = input("section: ")
    if x == "1":
        del store[dep][sec][input("item: ")]
    else:
        del store[dep][sec]


def search(store):
    while True:
        x = input("\n1. observe  2. add  3. delete  0. exit: ")
        match x:
            case "1":
                observe(store)
            case "2":
                add(store)
            case "3":
                remove(store)
            case "0":
                break
            case _:
                print("invalid option")


if __name__ == "__main__":
    store = {
        'groceries': {'meat': {}, 'fv': {}, 'dairy': {}, 'drinks': {}},
        'electronics': {'cleaning': {}, 'cooking': {}, 'gaming': {}},
    }
    search(store)
