##Actividad 11 

Primero de todo he realizado la creacion de mi base de datos : 

![image](https://github.com/user-attachments/assets/f458f3bd-91a7-4cda-8d94-4d11e398bc23)

Despues de esto, lo que he hecho ha sido empezar a crear todos los post: 

En primer lugar he creado un get de começar el joc y comprobar que funcione: 


![començar partida](https://github.com/user-attachments/assets/2144b1e5-896a-4709-b55b-59ed1e6a97ea)


2. he hecho renderizar el texto, comprobamos que funciones :

   ![Renderitzar text](https://github.com/user-attachments/assets/6e6c4187-d681-4282-8ed2-c7ed5cfe4c71)


3. He creado un post, donde estan las palabras, donde aparece el abecedario:
Lo ponemos en español:

 ![image](https://github.com/user-attachments/assets/0ef87704-82b3-46aa-85dc-b57133e15925)

 lo que me devuelve es lo siguiente : 
![image](https://github.com/user-attachments/assets/7d5b4b9b-5b1a-4f63-880a-e84781422878)

 4. El siguiente punto es el registrar intentos, es el que mas me ha costado : adjunto capura
primero de todo le paso unos valores para que me los busque en la base de datos :

 ![image](https://github.com/user-attachments/assets/b8fb9cbc-f3bd-4024-83bd-52b62207686c)

 el jugador con ese id es : 
![image](https://github.com/user-attachments/assets/43893b25-b5a2-491b-b3e1-b69ee4a13449)

palabra : 
![image](https://github.com/user-attachments/assets/52eeae75-ada1-4789-a8f1-55e068ca0e9a)

y al hacer esto me devolvera el siguinete registro que es lo que me aparecera en la bbdd: 

![image](https://github.com/user-attachments/assets/1fc29955-f805-402b-b463-fe11e60da55d)

lo que se guarda en la bbdd: 
![image](https://github.com/user-attachments/assets/3e35556c-0442-4ef3-997d-ba790999cb53)

luego tmb he creado un get donde muestro la infromacion del jugador : 
    ![image](https://github.com/user-attachments/assets/08b22e77-8124-41d1-b197-bc81d662a4a8)

   
y me muestra la siguiente informacion del jugador:
![image](https://github.com/user-attachments/assets/454e1a87-4453-457e-9053-f97abf5ef4d0)


tambien he creado un post de insertar jugador : 


![image](https://github.com/user-attachments/assets/5e5fa9d3-8d85-48b9-8f13-79566eae1cc9)

y me se agrega ortogandole un id automatico: 

![image](https://github.com/user-attachments/assets/24563a7e-e6eb-4cb7-bb8a-6574207476ac)

Luego quiero obtener la informacion de ese jugadro insertado :
![image](https://github.com/user-attachments/assets/37b48038-1b4f-4bc3-8546-2f79a68ed5d6)

![image](https://github.com/user-attachments/assets/731231f2-4023-495d-b38c-a30fff6a8051)


Luego he creado un post para insertar categoria : 
![image](https://github.com/user-attachments/assets/f1a2f286-d8b9-4f3f-a418-7b3abb034e31)

![image](https://github.com/user-attachments/assets/adc9bd5e-e499-4826-97f7-b14d89783bf2)

Se me agrega a la bbdd correctamente : 
![image](https://github.com/user-attachments/assets/1b4da04b-71a7-400b-a0f1-3e267f2b8144)

 Luego si quiero obtener esa categoria hago lo un get : 
 
![image](https://github.com/user-attachments/assets/9c867cdd-f7e7-4af1-afe3-717c81b599e2)

 
Por ultimo, si queremos ver todas las categorias creo un get: 

![image](https://github.com/user-attachments/assets/15b1fdfb-10d5-41f9-af8d-4839585883f2)


## En la practica Anterior habia creado el insert y read, asi que ahora solo tendre que añadir del crud el update y delete: 

UPDATE: 

Voy a querer cambiar el jugador con id 11, que es enric, en mi bbdd aparece lo siguiente : 

![image](https://github.com/user-attachments/assets/c693482f-db94-48a5-947b-caa82ef620ac)

Actualizandolo : 

![image](https://github.com/user-attachments/assets/6047b1c6-8576-469e-b607-9e884d42d37d)
![image](https://github.com/user-attachments/assets/b00663fc-b723-4b26-a358-a07d9fb36774)
Comprobadno en mi bbd: 

![image](https://github.com/user-attachments/assets/fd426ca1-f23b-4097-aabb-fdca083f9f23)

Categoria :  sofa con id 43 la voy a cambiar a inmobiliario : 

![image](https://github.com/user-attachments/assets/37cb23cc-debd-45bd-bb3e-521f3eb1fd51)
![image](https://github.com/user-attachments/assets/afb97929-c14d-451e-abdd-33cbc0e3482c)
![image](https://github.com/user-attachments/assets/b5166765-6ef3-49a3-a8cf-20f104852e14)

en mi bbdd : 

![image](https://github.com/user-attachments/assets/fa222b25-01bb-4a8d-9e92-ff126175ca92)


Palabra turron con id 5 : 

![image](https://github.com/user-attachments/assets/54bb4865-3a84-4daa-893b-2a23cb9953ae)
![image](https://github.com/user-attachments/assets/3fe1c3a6-4f61-4a7b-a832-a04828e9bd8f)
![image](https://github.com/user-attachments/assets/a18f9d05-b9f2-4411-8f97-6558484cba69)

EN MI BBDD: 

![image](https://github.com/user-attachments/assets/5897436d-ab84-46cf-9ba6-448b3c135404)

DELETE: 

Pasamos a elimnar a un jugadro voy a eliminar a roberto Trujillo: 

![image](https://github.com/user-attachments/assets/e21f5199-b27b-4d0e-8b2f-0b2cbb027db4)

lo hacemos en fastapy : 

![image](https://github.com/user-attachments/assets/0e23936f-9654-4406-9b29-73d416e91af6)
![image](https://github.com/user-attachments/assets/6b7ef877-278b-4c72-a939-05a5591e9413)


Ahora nos vamos a nuestra bbdd para comprobra que se ha elimando : 

![image](https://github.com/user-attachments/assets/04d7dda6-5aa7-4820-aba2-9adf16e60ba3)

como podemos ver, se ha elimado.

ELIMINAR CATEGORIA : 
Voy a elimnar categoria 46 inserts

![image](https://github.com/user-attachments/assets/dc879226-f639-41f0-a609-89f72ed9bc3c)

lo hacemos en fatapy: 
![image](https://github.com/user-attachments/assets/11f4b4de-f80b-4689-8b55-d97d51540247)

como podemos ver a continuacion no aparecer : 
![image](https://github.com/user-attachments/assets/33100743-453b-4ef7-937d-8faaf490dee2)

Pasamos a elimnar palabras : 
como podemos observar hay muchos elefantes, eliminare el que tiene el id 11:
![image](https://github.com/user-attachments/assets/06434e61-b961-48c8-934d-6754e2523bd8)

Como podemos observar se ha elimnado correctamente: 

![image](https://github.com/user-attachments/assets/952818ab-02c2-4029-a848-5386d3cfc3da)
![image](https://github.com/user-attachments/assets/107efaab-e638-41f1-9384-fb3b3c81e860)





