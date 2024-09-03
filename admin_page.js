      // 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정합니다.
      // 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리르 작성해 볼 수 있음
      const data = [
        { category: "상의", brand: 'Supreme', product: '슈프림 박스로고 후드티', price: '390,000' },
        { category: "하의", brand: 'DIESEL', product: '디젤 트랙 팬츠', price: '188,000' },
        { category: "신발", brand: 'Nike', product: '에어포스 1', price: '137,000' },
        { category: "패션잡화", brand: 'Music&Goods', product: '빵빵이 키링', price: '29,000' },
        // ...
    ];
    
    const dataTable = document.getElementById('data-table');
    
    data.forEach((item) => {
        const row = dataTable.insertRow();
        row.insertCell(0).innerHTML = item.category;
        row.insertCell(1).innerHTML = item.brand;
        row.insertCell(2).innerHTML = item.product;
        row.insertCell(3).innerHTML = item.price;
    });

    //시간 불러오는 함수를 만들어보자
    function updateTime(){
        const now = new Date();//현재의 날짜와 시간을 가져온다.
        const dateString = now.toLocaleDateString('ko-KR'); // yyyy-mm-dd 형식으로 포멧한다.
        const timeString = now.toLocaleTimeString('ko-KR'); // hh:mm:ss AM/PM 형식으로 포멧한다.

        //date-time 요소에 날짜와 시간 문자열을 설정한다.
        document.getElementById('date-time').innerHTML = `현재 날짜: ${dateString} <br> 현재 시간: ${timeString}`;
    }

    // 1초마다 updateTime 함수를 호출하여 실시간으로 시간을 업데이트한다.
    setInterval(updateTime, 1000);


//부트스트랩에서 가져온 다크모드 토글용 
(() => {
'use strict'

const getStoredTheme = () => localStorage.getItem('theme')
const setStoredTheme = theme => localStorage.setItem('theme', theme)

const getPreferredTheme = () => {
  const storedTheme = getStoredTheme()
  if (storedTheme) {
    return storedTheme
  }

  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

const setTheme = theme => {
  if (theme === 'auto') {
    document.documentElement.setAttribute('data-bs-theme', (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'))
  } else {
    document.documentElement.setAttribute('data-bs-theme', theme)
  }
}

setTheme(getPreferredTheme())

const showActiveTheme = (theme, focus = false) => {
  const themeSwitcher = document.querySelector('#bd-theme')

  if (!themeSwitcher) {
    return
  }

  const themeSwitcherText = document.querySelector('#bd-theme-text')
  const activeThemeIcon = document.querySelector('.theme-icon-active use')
  const btnToActive = document.querySelector(`[data-bs-theme-value="${theme}"]`)
  const svgOfActiveBtn = btnToActive.querySelector('svg use').getAttribute('href')

  document.querySelectorAll('[data-bs-theme-value]').forEach(element => {
    element.classList.remove('active')
    element.setAttribute('aria-pressed', 'false')
  })

  btnToActive.classList.add('active')
  btnToActive.setAttribute('aria-pressed', 'true')
  activeThemeIcon.setAttribute('href', svgOfActiveBtn)
  const themeSwitcherLabel = `${themeSwitcherText.textContent} (${btnToActive.dataset.bsThemeValue})`
  themeSwitcher.setAttribute('aria-label', themeSwitcherLabel)

  if (focus) {
    themeSwitcher.focus()
  }
}

window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
  const storedTheme = getStoredTheme()
  if (storedTheme !== 'light' && storedTheme !== 'dark') {
    setTheme(getPreferredTheme())
  }
})

window.addEventListener('DOMContentLoaded', () => {
  showActiveTheme(getPreferredTheme())

  document.querySelectorAll('[data-bs-theme-value]')
    .forEach(toggle => {
      toggle.addEventListener('click', () => {
        const theme = toggle.getAttribute('data-bs-theme-value')
        setStoredTheme(theme)
        setTheme(theme)
        showActiveTheme(theme, true)
      })
    })
})
})()
      
/*도와줘요 지피티*/
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-bs-theme-value]').forEach(toggle => {
        toggle.addEventListener('click', () => {
            const theme = toggle.getAttribute('data-bs-theme-value');
            setStoredTheme(theme);
            setTheme(theme);
            showActiveTheme(theme, true);
        });
    });
});

function showActiveTheme(theme, focus = false) {
    const themeLightIcon = document.querySelector('.theme-icon-light');
    const themeDarkIcon = document.querySelector('.theme-icon-dark');
    
    if (theme === 'dark') {
        themeLightIcon.style.display = 'none';
        themeDarkIcon.style.display = 'inline-block';
    } else {
        themeLightIcon.style.display = 'inline-block';
        themeDarkIcon.style.display = 'none';
    }
}
/*고마워요 지피티*/