export default {

  //cookie
  addCookie,
  getCookie,

}

//Cookies
function addCookie(k, v, time) {
  let date = new Date();
  date.setTime(date.getTime() + time);
  document.cookie = k + '=' + v + ";expires=" + date;
}

function getCookie(k) {
  let cookie = document.cookie;
  let list = cookie.split('; ');
  for (let i = 0; i < list.length; i++) {
    let temp = list[i].split('=');
    if (temp[0] === k) {
      return temp[1];
    }
  }
}
