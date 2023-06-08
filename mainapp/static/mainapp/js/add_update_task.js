function createTask(){
	name = document.getElementById("input_task_name").value
	repeat = document.getElementById("selected-repeat").innerHTML
	priority = document.getElementById("selected-priority").innerHTML
	time = document.getElementById("start_time").value

	console.log(name, repeat, priority, time)
	
	fetch("/api/task", {
	    	method: 'POST',
	    	headers: {
	                'Content-Type': 'application/json',
	            },
	    	body: JSON.stringify({
	    		task_name: name,
	    		repeat: repeat,
	    		priority: priority,
	    		start_time: time,
	    	})
		}).then(res => {
			if (res.ok) {
			alert('successful');
			}
			else{
				alert('not found');
			}
		})
		.then(data => console.log(data))
		.catch(error => console.log('ERROR'))

	window.location.href = 'http://localhost:8000/';
}

function updateTask(task_id) {

	name = document.getElementById("input_task_name").value
	repeat = document.getElementById("selected-repeat").innerHTML
	priority = document.getElementById("selected-priority").innerHTML
	time = document.getElementById("start_time").value

	console.log(name, repeat, priority, time)
	
	fetch("/api/task/" + task_id, {
	    	method: 'PUT',
	    	headers: {
	                'Content-Type': 'application/json',
	            },
	    	body: JSON.stringify({
	    		task_name: name,
	    		repeat: repeat,
	    		priority: priority,
	    		start_time: time,
	    	})
		}).then(res => {
			if (res.ok) {
			alert('successful');
			}
			else{
				alert('not found');
			}
		})
		.then(data => console.log(data))

	window.location.href = 'http://localhost:8000/';
	
}

$('#dropdown-repeat a').click(function(){
    $('#selected-repeat').text($(this).text());
  });

$('#dropdown-priority a').click(function(){
	$('#selected-priority').text($(this).text());
});