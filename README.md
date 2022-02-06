<h1>AirBnB Clone</h1>
<p>This is the first step towards building your first full web application: the AirBnB clone.</p>
<p>This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…</p>
<hr />
<p>Each task is linked and will help you to:</p>
<ol>
<li>put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file</li>
<li>create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel</li>
<li>create the first abstracted storage engine of the project: File storage.</li>
<li>create all unittests to validate all our classes and storage engine</li>
</ol>
<hr />
<h2>The classes</h2>
<p>We first create a Parent class called <strong>BaseModel</strong>.</p>
<ol>
<p>It has 3 public instances</p>
<ol>
<li><em>id</em><ul>
<li>This attribute is a string. It uses <em>uuid</em> to generate random,id that will give each BaseModel unique id</li></ul></li>
<li><em>created_at</em><ul>
<li>This attribute is in datetime format. It will use <em>datetime</em> to generate the exact time the BaseModel instance was created</li></ul></li>
<li><em>updated_at</em><ul>
<li>This attribute is in datetime format. It will use <em>datetime</em> to generate the exact time the BaseModel instan
ce was updated</li></ul></li>
</ol>
<p>It also has 2 public instances and it will also have its own representation of __str__</p>
<ol>
<li><strong>save</strong><ul>
<li>This function will be called if there was adjustment to the instance such as updating attributes or deleting them</li></ul></li>
<li><strong>to_dict</strong><ul>
<li>This function will return a dictionary of all keys and values of __dict__. New key __class__ will be added whose value is the name of the class. In this function the datetime attributes mentioned above will be converted to their string version in the format of %Y-%m-%dT%H:%M:%S.%f or 2017-06-14T22:31:03.285259</li></ul></li>
<li><strong>__str__</strong><ul>
<li>This function will print the string representation in form of <q>[<class name>] (<self.id>) <self.__dict__></q></li></ul></li>
</ol>
<hr />
<p>Lets see examples that sum up the BaseModel class</p>
<p>my_model = BaseModel()</p>
<p>my_model.name = "My First Model"</p>
<p>my_model.number = 89</p>
<p>print(my_model)</p>
<p>my_model.save()</p>
<p>print(my_model)</p>
<p>my_model_json = mymodel.to_dict()</p>
<p>print(mymodel_json)</p>
<strong>Result</strong>
<p>[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}</p>
<p>[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}</p>
<p>{'number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}</p>
<hr />
<p>BaseModel also handles "kwargs"</p>
<p>The args will not be used but when kwargs is given it will return the changes made by to_dict function to their original __dict__ version. This means __class__ will be removed, the datetimes will be converted to tehir datetime format.</p>
<p>Let us use the above example</p>
<p>new_model = BaseModel(mymodeljson)</p>
<p>print(new_model)</p>
<strong>Result</strong>
<p>[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}</p>
<h2>The File Storage</h2>
<p>We will the proceed to creatig a storage file that will have the class <strong>FileStorage</strong></p>
<p>This file storage will work on serilization and deserilization of json file, where all instances created will be stored and retrived from.</p>
<p>It consists of two private class attributes.</p>
<ol>
<li><strong>__file_path</strong><ul>
<li>This attribute is a string whose value is the name of the json file</li></ul></li>
<li><strong>__objects</strong><ul>
<li>This attribute is a dictionary and it will store all the attributes created in the format of <q>{<class name>.id: instance}</q></li></ul></li>
</ol>
<p>It consists of 4 functions.</p>
<ol>
<li><strong>all</strong><ul>
<li>This function will return dictionary stored in FileStorage.objects</li></ul></li>
<li><strong>new</strong><ul>
<li>This function will take an instance and takes the name and id to make <q><class name>.id</q> which will the use it as a key to assign it the instance as a value to be stored in objects instance.</li>
<li>This function will be called in the basemodel every time a new instance is called.</li></ul></li> 
<li><strong>save</strong><ul>
<li>This function will store the dictionary objects instance into the json path indicated by file_path</li>
<li>This function will be called in the BaseModel function save(), so whenever the instance is changed it will be saved and that saved instance will also be updated on the json file</li></ul></li>
<li><strong>reload</strong><ul>
<li>This function will read from json file and convert it to the form of dictionary that objects instance uses.</li>
<li>This function will be called inside the __init__ .py file</li></ul></li>
</ol>
<p>Let us see this as a continuation of the above example. Note my_model.save() was called in the above example</p>

<p>all_objs = storage.all()</p>
<p>for obj_id in all_objs.keys():</p>
<p>    obj = all_objs[obj_id]</p>
<p>    print(obj)</p>
<strong>Result</strong>
<p>[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}</p>

<p>let us create another one</p>

<p>model = BaseModel()</p>
<p>model.name = "last name"</p>
<p>model.my_number = 100</p>
<p>model.save()</p>

<p>Now let us call the storage.all() as above</p>

<p>all_objs = storage.all()</p>
<p>for obj_id in all_objs.keys():</p>
<p>    obj = all_objs[obj_id]</p>
<p>    print(obj)</p>
<strong>Result</strong>
<p>[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}</p>
<p>[BaseModel] (s9r6r89g-o97p-9453-3h89-1d586975u589) {'number': 100, 'name': 'last name', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 54, 110434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 54, 114778)}</p>
<p>We can now see that two instances are stored in storage or json file</p>
<h2>The console</h2>
<p>This console acts like a shell, but limited to a specific use-case. In our case, we want to be able to manage the objects of our project.</p>
<ol>
<p>It has 5 properties</p>
<ol>
<li><strong>Create</strong><ul>
<li>Creates a new instance, saves it (to the JSON file) and prints the id</li></ul></li>
<li><strong>Show</strong><ul>
<li>Prints the string representation of an instance based on the class name and id</li></ul></li>
<li><strong>All</strong><ul>
<li>Prints all string representation of all instances based or not on the class name</li></ul></li>
<li><strong>Destroy</strong><ul>
<li>Deletes an instance based on the class name and id (save the change into the JSON file).</li></ul></li>
<li><strong>Update</strong><ul>
<li>Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)</li></ul></li>
</ol>
<p>It also has quit and EOF properties for exiting the console.</p>
<hr />
<p>Now we will see the console in action</p>
<p>./console</p>
<p>(hbtn) </p>
<p>(hbtn) create BaseModel</p>
<p>49faff9a-6318-451f-87b6-910505c55907</p>
<p>(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907</p>
<p>[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}</p>
<p>(hbnb) all BaseModel</p>
<p>\["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]</p>
<p>(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"</p>
<p>(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907</p>
<p>[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}</p>
<p>(hbnb) create BaseModel</p>
<p>2dd6ef5c-467c-4f82-9521-a772ea7d84e9</p>
<p>(hbnb) all BaseModel</p>
<p>\["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]</p>
<p>(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907</p>
<p>(hbnb) all BaseModel</p>
<p>\["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]</p>

<p>We hope You enjoy it.</p>

<p><strong>Authors</strong></p>
<ol>
<li>Opeyemi Ogunbode</li>
<li>Samra Barnabas</li>
</ol>
