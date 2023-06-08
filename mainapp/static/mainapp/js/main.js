fetch("/api/task")
	.then(res => res.json())
	.then(data => {
		tasks = data["tasks"]

		for(let i = 0; i < tasks.length; i++){
			const item = tasks[i].name;
			const id = tasks[i].id;
			addTask(item, id);
		}
	})

function addTask(name, task_id) {		
	var html = `<div class="card">
				  <div class="card-body">
				    <a href="/update/task/` + task_id + `">` + name + `</a>
				    <a onclick="deleteTask(` + task_id + `)"><i class="bi bi-x-lg"></i></a>	
				  </div>
				</div>`
	task_list_div = document.getElementById("today_list");
	task_list_div.innerHTML += html;
}


document.getElementById("form1")
  .addEventListener('change', (e) => {
	input_value = document.getElementById('form1').value
  	task_list_div = document.getElementById("today_list")
  	task_list_div.innerHTML = ""
  	console.log(input_value)
    fetch("/api/search", {
    	method: 'POST',
    	headers: {
                'Content-Type': 'application/json',
            },
    	body: JSON.stringify({
    		task_name: input_value
    	})
	}).then(res => {
		if (res.ok) {
			alert('successful');
		}
		else{
			alert('not found');
		}
	})
	.then(data => {
		tasks = data["tasks"]
		console.log(tasks)
		for(let i = 0; i < tasks.length; i++) {
			const item = tasks[i].name;
			filterTask(item);
		}
	})
 });

function filterTask(name) {		
	var html = `<div class="card">
				  <div class="card-body">
				    <a href="#">` + name + `</a>
				  </div>
				</div>`
	task_list_div = document.getElementById("today_list");
	task_list_div.innerHTML += html;
}

function deleteTask(task_id) {
	fetch('/api/task/' + task_id, {
		method: "DELETE",
		headers: {
			'Content-Type': 'application/json'
		},
	}).then(res => res.json())
		.then(data => {
			message = data["message"]
			alert(message);
		})

}

function my_info() {
	profile_name_div = document.getElementById('profile-name')
	fetch('me/api')
	.then(res => res.json())
	.then(data => {
		user = data["user"]
		number = user.phone_no
		profile_name_div.innerHTML = `<h5 style="">` + number + `</h5>`
	})
}

my_info();

function showAddTask()
{
  document.getElementById('add-task-container').style.visibility = "visible";
}