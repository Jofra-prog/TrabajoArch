
# 1 Ejercicio
 En este ejercicio defino dos funciones. 

Una donde lee el archivo .csv y lo coloca en una lista leyendo las lineas, define los encabezados en "encabezados"con la linea 0, luego crea un diccionario "datos" donde se van a añadir los elementos de la lista "lineasar" desde la linea 1 creando este diccionario con el metodo zip() que asigna un encabezado al valor iterado en "lineasar" y luego con el metodo append lo añade al diccionario "datos".

La segunda funcion genera una lista "compras_pais" donde asigna a "fila" una iteracion en el diccionario creado "datos", si en la diccionario se encuentra fila['Contry'] igual al pais que ingresamos añade este a la lista "compras_pais" y una vez termina la iteracion retorna esta lista.

Al final coloco un metodo try para que ingrese la ruta del archivo donde quiere encontrar la informacion, si no esta el archivo no se rompe el ciclo whilem da el mensaje de error y vuelve a que ingrese la ruta del archivo. Y otro ciclo para que ingrese la ruta del pais que queire buscar, si esta el pais retorna la longitud de la lista "compras_pais" y es la canntidad que fue la cantidad que se compras que hay en ese pais, si no esta imprime que el pais no esta en la lista y que lo escriba de nuevo.


[![Screenshot-2025-02-24-010749.png](https://i.postimg.cc/bvgWY3nC/Screenshot-2025-02-24-010749.png)](https://postimg.cc/FffDDbD3)



# 2 Ejercicio
 En este ejercicio es el mismo anterior, no mas hay cambios cuando busca en el diccionario es en fila['Payment_Type'], y al momento de ingresar informacion pide que ingrese el metodo de pago a buscar en vez del pais, pero las funciones son exactamente las mismas.
 
 
 [![Screenshot-2025-02-24-011134.png](https://i.postimg.cc/rFGvYVm2/Screenshot-2025-02-24-011134.png)](https://postimg.cc/qzRbNdy1)

