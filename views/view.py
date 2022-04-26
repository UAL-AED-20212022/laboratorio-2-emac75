from models.LinkedList import LinkedList

def main():
    lista_ligada = LinkedList()
    while True:
        #Faz split do input por espaco ex: comandos[0],comandos[1],comandos[2],... 
        try:
            comandos :list = input().split(" ")
        except EOFError:
            return
        if comandos[0] == "RPI": #Registar inicio da lista
            lista_ligada.insert_at_start(comandos[1])
        elif comandos[0] == "RPF": #Registar no fim da lista
            lista_ligada.insert_at_end(comandos[1])
        elif comandos[0] == "RPDE": #Registar depois de outro elemento
            lista_ligada.insert_after_item(comandos[2],comandos[1])
        elif comandos[0] == "RPAE": #Registar antes de outro elemento
            lista_ligada.insert_before_item(comandos[2],comandos[1])
        elif comandos[0] == "RPII": #Registar num determinado indice
            lista_ligada.insert_at_index(int(comandos[2]),comandos[1])
        elif comandos[0] == "VNE": #Verificar numero de elementos
            print("O número de elementos são " + str(lista_ligada.get_count()))
        elif comandos[0] == "VP": #Verificar se pais se encontra na lista
            if lista_ligada.search_item(comandos[1]) == False:
                print("O país "+str(comandos[1])+" não se encontra na lista")
            else:
                print("O país " + str(comandos[1]) + " encontra-se na lista")
        elif comandos[0] == "EPE": #Eliminar primeiro elemento
            print("O país "+ lista_ligada.start_node.get_item() +" foi eliminado da lista.") 
            lista_ligada.delete_at_start()
        elif comandos[0] == "EUE": #Eliminar ultimo elemento
            print("O país "+ lista_ligada.get_last_node() +" foi eliminado da lista.") 
            lista_ligada.delete_at_end()
        elif comandos[0] == "EP": #Eliminar determinado pais
            if lista_ligada.search_item(comandos[1]) == False:
                print("O país "+str(comandos[1])+" não se encontra na lista")
            else:
                print("O país "+str(comandos[1])+" foi eliminado da lista")
                lista_ligada.delete_element_by_value(comandos[1])
        else:
            if comandos[0] == "":
                break
        #print lista
        lista_ligada.traverse_list()
    