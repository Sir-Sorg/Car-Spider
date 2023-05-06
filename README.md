# Car-Spider 🕷
This program performs the following activities using 4 sub-programs of Python:
- Web scraping using `requests` and receiving data from the web
- Analyzing and storing information in the database with `sqllite`
- Retrieving information from the database and Learning `regression` on them
- Get information along with a graphical interface using `PyQt‍‍`
## Program Structure ⛩
At the beginning, we use the ‍`Spider.py` program to analyze the information from the **bama** website.
In the next step, after analyzing the obtained information, we save it in the database using ‍`sqllite` This operation is done inside the `Storage.py` file.
In the next step, we re-read the information from the database and by coding the categorical features into numbers and normalizing them, we prepare it for training by `KNNRegression‍` in `Foreteller.py`.
The `Car_Spider_Ui.py` file has the task of displaying the graphical interface and receiving information from the user, and after receiving the user's information, it gives it to the small program and controller `Car_Price_Predict.py` and displays the output in itself.

You can see the general structure of this process in the image below

![structure](https://user-images.githubusercontent.com/66873974/236615790-c2b786a7-e324-4e74-b9e4-7cc591560314.jpg)
## Database 💾
The database has 9 features, **Id**, **color**, ... and final **price** The structure of the database is very simple and is simulated using ‍`sqlite`, which easily executes sql commands on it

![db](https://user-images.githubusercontent.com/66873974/236616024-4740e5f1-53a6-45b7-8ff5-82a9e9a735da.png)
## Machine learning 📌
We use **KNeighborsRegressor** regression to teach information to the machine. You can read about how it works from this [sklearn neighbors](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html).

![KNeighborsRegressor](https://user-images.githubusercontent.com/66873974/236616372-d9880400-4f9f-46a8-9b32-7ac9ccb79de6.png)
# Application 🖥
Finally, the graphic interface of our program with *purple color* is shown below, which is suitable for receiving sample information for `Samand` cars, easily by changing *two lines* of code, it is possible to download all cars and store them in the database, as well as determine the price of all of them, which is possible because of the index. I did not make more than 200 pages of this activity so that only the functionality of the program was tested.

![Project-UI](https://user-images.githubusercontent.com/66873974/236616961-30b9c62f-a7e8-45a3-b56d-f17231b5c17b.png)

If you have any questions or find a bug in the program, please contact me via email: *sinaorojlo53@gmail.com*.
