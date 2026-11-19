from queue import Queue

IGIC = 0.07  # General IGIC rate: 7 %

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
                parseToTxt(store)
                break
            case _:
                print("invalid option")

def parseToTxt(store: dict) -> None:
    '''
    Converts a dictionary with the specific structure of this database into a single line of text
    that is then stored into a text file so it persists.

    :param store:
    :return:

    Marcos Caburrasi Segundo
    '''

    q: Queue[dict[str, object]] = Queue(maxsize=0)
    q.put(store)
    string_builder: str = ""

    while not q.empty():
        '''
        BFS the dictionary tree and store it in order
        '''
        node: object = q.get()
        string_builder_2 = ""

        for x, y in node.items():
            '''
            If its a leaf, add the name-value pair and stop adding to the queue
            '''
            if len(x) > 0:
                add_y = ""
                if type(y) != dict:
                    add_y = "-" + y
                string_builder_2 += f":{x}{add_y}"

                if type(y) == dict:
                    q.put(y)

        '''
        Treat the string so it's more readable by removing unnecesary separators
        '''
        string_builder += string_builder_2[1:]
        string_builder += "|"

    '''
    Write to file
    '''
    with open("db.txt", "w", encoding="utf-8") as f:
        f.write(string_builder[:-1].strip("|"))

def parseToMap() -> dict[str, object]:
    '''
    converts the text from the db.txt file to a dictionary with the same given structure by BFS
    :return:
    Marcos Caburrasi Segundo
    '''

    '''
    Read the file and split it to make it a list of lists, so it's easier
    to iterate
    '''
    string_builder: str
    with open("db.txt", "r", encoding="utf-8") as f:
        string_builder = f.read()

    list_of_db: list = string_builder.split("|")
    final_list_of_db: list = []

    for element in list_of_db:
        final_list_of_db.append(element.split(":"))


    '''
    make the dictionary and prepare the 2 main branches for the iteration using
    BFS
    '''
    store: dict[str, object] = {}

    q: Queue = Queue(maxsize=0)
    index: int = 0
    for element in final_list_of_db[0]:
        store[element] = {}
        q.put(store[element])

    index += 1

    while not q.empty():
        current_branch: dict[str, object] = q.get()

        '''
        if i is a name-value pair, add it to as a leaf and stop with that specific branch,
        else, keep iterating the branches,
        if name-value pair is empty (represented by "||" 2 pipes) don't add anything to that branch and end it
        '''
        try:
            for i in final_list_of_db[index]:
                if "-" in i:
                    l: list[str] = i.split("-")
                    current_branch[l[0]] = l[1]
                elif len(i) > 0:
                    current_branch[i] = {}
                    q.put(current_branch[i])

            index += 1
        except IndexError:
            break

    return store

def to_price(value):
    """Convert a price stored as text ("1.20" or "1,20") to a number. Return None if it isn't one."""
    try:
        return float(str(value).strip().replace(",", "."))
    except ValueError:
        return None


def find_item(store, name):
    """
    Traverse the store depth-first (DFS): department -> section -> item.
    A leaf is a pair item_name: price. Return [name, price], or None if not found.
    """
    wanted = name.strip().lower()
    for key, value in store.items():
        if isinstance(value, dict):
            found = find_item(value, name)
            if found:
                return found
        elif key.strip().lower() == wanted:
            price = to_price(value)
            if price is not None:
                return [key, price]
    return None


def add_item(cart, item):
    """Add the item [name, price] to the cart."""
    if item:
        cart.append(item)
    else:
        print("Item not found")


def calculate_price(cart):
    """Print the cart with subtotal, IGIC and total. Return the total."""
    subtotal = 0
    for name, price in cart:
        print(f"{name:<15}{price:>8.2f} €")
        subtotal += price

    tax = subtotal * IGIC
    total = subtotal + tax

    print("-" * 23)
    print(f"{'Subtotal':<15}{subtotal:>8.2f} €")
    print(f"{'IGIC (7%)':<15}{tax:>8.2f} €")
    print(f"{'TOTAL':<15}{total:>8.2f} €")
    return total

if __name__ == "__main__":
    store = parseToMap()

    while True:
        choice: str = input("What do you want to do?\n 1. Check database 2. Make receipt 0. Exit ")
        match choice:
            case '1':
                search(store)
            case '2':
                cart: list[list] = []
                while True:
                    wanted: str = input("What now? 1.Add item (write item name) 0. exit ")
                    match wanted:
                        case '0':
                            break
                        case _:
                            item = find_item(store, wanted)
                            add_item(cart, item)

                calculate_price(cart)

            case '0':
                break
