import axios from 'axios'
import qs from "qs";
import router from '../router/index'
import api from "./api";

axios.defaults.baseURL = "http://localhost:8071";
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.get['Content-Type'] = 'application/json';
axios.defaults.headers.delete['Content-Type'] = 'application/json';
axios.defaults.headers.put['Content-Type'] = 'application/json';
axios.defaults.timeout = 0;
const authorizationPrefix = 'bearer';

axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 403:
          router.push({name: '403'});
          break;
        case 401:
          if(error.response.data.error==='invalid_token'){
            api.addCookie("token","");
            location.reload();
          }
          else{
            router.push({name:'Login'});
          }
          break;
        case 400:
          if(error.response.data.error==='invalid_token'){
            break;
          }
      }
    }
    return Promise.reject(error);
  }
);



function parseParamToString(params) {
  if (params !== undefined) {
    let s = '?';
    for (let param in params) {
      if (!params.hasOwnProperty(param)) {
        continue;
      }
      s += (param + "=" + params[param] + "&")
    }
    return s;
  }
  return '';
}

export default {
  post(url,param,requireAuth){
    const token = api.getCookie("token");
    let request = {
      method: "POST",
      url: url,
      data: param,
    };
    if(requireAuth&&token!==undefined&&token!==''&&token.length!==0){
      request.headers = {'authorization':authorizationPrefix + token}
    }
    return axios(request);
  },
  postFormData(url, param, obj,title,requireAuth) {
    const token = api.getCookie("token");
    let request = {
      method: "POST",
      url: url,
      data: param,
      onUploadProgress: function (progressEvent) {
        if (progressEvent.lengthComputable) {
          obj.$root.eventBus.$emit(title+'-progress', {number: progressEvent.loaded / progressEvent.total * 100})
        }
      },
      headers: {
        'Content-Type': 'multipart/form-data',
        'authorization':authorizationPrefix + api.getCookie("token")
      }
    };
    if(requireAuth&&token!==undefined&&token!==''&&token.length!==0){
      request.headers = {'authorization':authorizationPrefix + token}
    }
    return axios(request)
  },
  get(url, param,requireAuth) {
    const token = api.getCookie("token");
    let request = {
      method: "GET",
      url: url + parseParamToString(param)
    };
    if(requireAuth&&token!==undefined&&token!==''&&token.length!==0){
      request.headers = {'authorization':authorizationPrefix + token}
    }
    return axios(request)
  },
  delete(url,param,requireAuth){
    const token = api.getCookie("token");
    let request = {
      method: "DELETE",
      url: url,
      data: param
    };
    if(requireAuth&&token!==undefined&&token!==''&&token.length!==0){
      request.headers = {'authorization':authorizationPrefix + token}
    }
    return axios(request)
  },
  put(url, param,requireAuth) {
    const token = api.getCookie("token");
    let request = {
      method: "PUT",
      url: url,
      data: qs.stringify(param)
    };
    if(requireAuth&&token!==undefined&&token!==''&&token.length!==0){
      request.headers = {'authorization':authorizationPrefix + token}
    }
    return axios(request)
  },
  patch(url, param,requireAuth) {
    const token = api.getCookie("token");
    let request = {
      method: "PATCH",
      url: url,
      data: qs.stringify(param)
    };
    if(requireAuth&&token!==undefined&&token!==''&&token.length!==0){
      request.headers = {'authorization':authorizationPrefix + token}
    }
    return axios(request)
  }
}
