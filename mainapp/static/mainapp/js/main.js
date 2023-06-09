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
	var html = `<div class="card shadow m-3 mb-3 border-0" style="transition: transform 200ms ease 0s;">
				    <a href="/update/task/` + task_id + `"><div class="card-body">` + name + `</div></a>
				    <a onclick="deleteTask(` + task_id + `)" style="position:absolute;z-index:2;right:5%; top:30%;"><i class="bi bi-x-lg"></i></a>	
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
	}).then(res => res.json())
		.then(data => {
			tasks = data["tasks"]
			console.log(tasks)

			for(let i = 0; i < tasks.length; i++) {
				const item = tasks[i].name;
				const id = tasks[i].id;
				filterTask(item, id);
			}
		})
 });

function filterTask(name, task_id) {		
	var html = `<div class="card shadow m-3 mb-3 ">
				  <div class="card-body">
				    <a href="/update/task/` + task_id + `">` + name + `</a>
				    <a onclick="deleteTask(` + task_id + `)"><i class="bi bi-x-lg"></i></a>	
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
	window.location.href = '/';
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

