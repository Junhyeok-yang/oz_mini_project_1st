// 제출 이벤트를 받는다

//제출된 입력 값들을 참조한다.

//입력값에 문제가 있는 경우 이를 감지한다

//가입 환영 인사를 제공한다

const form = document.getElementById('form')

form.addEventListener('submit', function(event) {
    event.preventDefault() //기존 기능 차단

    let userid = event.target.id.value
    let userpw1 = event.target.pw1.value
    let userpw2 = event.target.pw2.value
    let useremail = event.target.email.value
    let userphone = event.target.phone.value
    let userposition = event.target.position.value
    let usergender = event.target.gender.value
    let username = event.target.name.value
    let userintro = event.target.intro.value


    if (userid.length < 6){
        alert('ID는 6자 이상 입력하세요.')
        return
    }

    if (userpw1 !== userpw2){
        alert('비밀번호가 일치하지 않습니다.')
        return
    }

//가입이 잘 되었다는 환영!
    document.body.innerHTML = ""
    document.write(`<p>${username}님, 환영합니다!</p>`)
    document.write('회원 가입 시 입력한 내역은 다음과 같습니다.')
    document.write(`<p>아이디 : ${userid}</p>`)
    document.write(`<p>이름 : ${username}</p>`)
    document.write(`<p>전화번호 : ${userphone}</p>`)
    document.write(`<p>원하는 직무 : ${userposition}</p>`)

})