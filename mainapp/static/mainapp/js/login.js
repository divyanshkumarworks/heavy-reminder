function getOtp() {

	form2_value = document.getElementById('form2').value
	form3_value = document.getElementById('form3').value
	input_value = form2_value + form3_value
	fetch('/api/get/otp', {
		method: "POST",
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			phone_number: input_value
		})
	}).then(res => res.json())
		.then(data => {
			items = data["OTPS"]
			const key = Object.keys(items)
			const user_num = key[0]
			const otp = items[user_num]
			verifyOtp(user_num, otp);
		})
}

function verifyOtp(num, otp) {
	var html = `<div>
					<div id="form-label">
	                  <h4>Please enter one time password to verify your account.</h4>
              		</div>
					<div class="input-form">
	                  <input type="text" id="form4" maxlength="1" class="form-control form-control-lg" max="1"
	                   style="width: 50px;padding: 3px; margin: 3px; text-align:center;" onkeyup="clickEvent(this,'form5')" />
	                </div>
	                <div class="input-form">
	                  <input type="text" id="form5" maxlength="1" class="form-control form-control-lg" max="1"
	                   style="width: 50px;padding: 3px; margin: 3px; text-align:center;" onkeyup="clickEvent(this,'form6')" />
	                </div>
	                <div class="input-form">
	                  <input type="text" id="form6" maxlength="1" class="form-control form-control-lg" max="1"
	                   style="width: 50px;padding: 3px; margin: 3px; text-align:center;" onkeyup="clickEvent(this,'form7')" />
	                </div>
	                <div class="input-form">
	                  <input type="text" id="form7" maxlength="1" class="form-control form-control-lg" max="1"
	                   style="width: 50px;padding: 3px; margin: 3px; text-align:center;" />
	                </div>
	                <div class="text-center pt-1 mt-5 pb-1">
		              <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="button" onclick="getToken()">verify</button>
		         
				</div>`
	login_form_div = document.getElementById('login-form')
	login_form_div.innerHTML = html
}

function getToken() {

	part1 = document.getElementById('form4').value
	part2 = document.getElementById('form5').value
	part3 = document.getElementById('form6').value
	part4 = document.getElementById('form7').value

	otp = part1 + part2 + part3 + part4
	
	fetch('api/login', {
		method: "POST",
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			otp: otp
		})
	}).then(res => {
		if(res.ok) {
			alert('successful!')
		}
		else{
			alert('not working')
		}
	}).then(data => {
		console.log(data);
	})

	window.location.href = '/';
}

function clickEvent(first,last){
  if(first.value.length){
    document.getElementById(last).focus();
  }
}