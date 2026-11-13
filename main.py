def search(store: dict) -> None:
    print ()
    x = input("introduce un valor")


    match x:
        case 0:
            print("")
        case 4:
            print()
        case _:
            print()
def add():
    pass

def remove():
    pass


if __name__ == "__main__":
    meat = {}
    fv = {}
    dairy = {}
    drinks = {}

    cleaning = {}
    cooking = {}
    gaming = {}

    groceries = {
        'meat': meat,
        'fv': fv,
        'dairy': dairy,
        'drinks': drinks
    }

    electronics = {
        'cleaning': cleaning,
        'cooking': cooking,
        'gaming': gaming
    }

    store = {
        'groceries': groceries,
        'electronics': electronics
    }
    '''
    { groceries {
            meats {
                chicken
                beef
                pork
            },
            fruit & veg {
                lettuce
                strawberry
                apples
            },
            dairy {
                whole fat milk
                yoghurt
                cheese
            },
            drinks {
                coke
                fanta
                lipton
            }
        },
        appliances {
            cleaning {
                roomba
                washing machine
                drier
            }
            cooking {
                oven
                microwave
                toaster
            }
            gaming {
                ps5
                xbox
                switch
            }
        }
    }
    
    '''