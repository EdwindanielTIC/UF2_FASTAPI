
Cometando documentació ***body-fields*** con postman.

He puesto la siguiente put con la siguiente url 
![PUT](https://github.com/user-attachments/assets/e6a40a69-a9c2-492f-8f9f-5eb3a1b22b6d)

Despues de ello me dirijo al body , selecciono la opcion Json y me aparece el texto, para que pueda funcionar, debo escribir la informacion que hay en el SWWAGER O escribirla yo directamente.
Como podemos comprobar con el POSTMAN , el codigo funciona.
![image](https://github.com/user-attachments/assets/49c40599-b77e-46df-85a7-776d99c6adf7)

***Body-Nested Models***
He realizado una prueba con el list : 

Como podemos observar, he añadido el id numero 100 y podemos ver que al ejecutarlo funciona correctamente

![image_list](https://github.com/user-attachments/assets/0e11df9f-1796-45ec-b117-06e375680c20)

El resultado que me devuelve es el siguiente : 

![image](https://github.com/user-attachments/assets/2dd76fa7-3745-44a3-9dff-52a091f8b566)

Tambien he realizado una prueba con set con la misma informacion :

![img_SET](https://github.com/user-attachments/assets/1deae3dd-ee75-41f4-85a3-ea3c5d05e351)

Como podemos observar en la siguiente imagen, el  parte del set, al introducir dos valores que son similares, me elima uno y se queda solo con uno, pero funciona correctamente.

![SET](https://github.com/user-attachments/assets/bc56f33c-46ad-4fe8-b9af-6d9dc3aca5e0)

A continuacion procederemos a realizar la coneccion con la base de datos: 
captura de que se conecto a la base de datos : 
![image](https://github.com/user-attachments/assets/c3259cb3-135c-411c-9235-0d3b366eb109)

foto de la creacion de la base de datos en pgAdmi: 
![image](https://github.com/user-attachments/assets/d7f156c8-f884-4a00-a179-a833629b14f0)


**INSERTANDO USUARIO**

A continuacion introduzco la siguinete infomracion : 
![image](https://github.com/user-attachments/assets/04d3755a-beb0-4d68-97df-cd1c8e599c9b)

Me devuelve la lista Json conforme se ma ha insertado correctamente el usuario : 

![image](https://github.com/user-attachments/assets/3404bccf-7673-4d36-a152-90463c06f3ce)

Procedemos a la verifica en pgAdmi que se haya insertado correctamente :

![image](https://github.com/user-attachments/assets/c210ec1f-ecae-454c-ba22-8dc693660ad4)

A continuacion lo que hago es el read. esto signfica que voy a buscar al usuario mediante su id, si este id existe me lo devolvera: 

![image](https://github.com/user-attachments/assets/d572e61f-75e0-43f3-8f19-0dbbd4aace60)

Se ha incertado correctamente.

diferencia entre usar el set y list 

![diferencia](image.png)


