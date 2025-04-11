import { ref, computed } from 'vue'
import axios, { AxiosError } from 'axios'


const token = ref(localStorage.getItem('token') || '')

const isAuthenticated = computed(() => !!token.value)

axios.defaults.headers.common['Authorization'] = `Token ${token.value}`

export const useAuth = () => {

  const signup = async (username: string, email: string, password: string) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/signup/', {
        username,
        email,
        password
      })
      

      localStorage.setItem('token', response.data.token)
      token.value = response.data.token
      axios.defaults.headers.common['Authorization'] = `Token ${token.value}`
      
      return true
    } catch (error) {
      if (error instanceof AxiosError) {
        throw new Error(error.response?.data.error || 'Erreur lors de l\'inscription')
      } else {
        throw new Error('Erreur inconnue lors de l\'inscription')
      }
    }
  }

 
  const loginUser = async (username: string, password: string) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/login/', {
        username,
        password
      })

      localStorage.setItem('token', response.data.token)
      token.value = response.data.token
      axios.defaults.headers.common['Authorization'] = `Token ${token.value}`
    } catch (error) {
      if (error instanceof AxiosError) {
        throw new Error(error.response?.data.error || 'Erreur de connexion, veuillez vérifier vos identifiants')
      } else {
        throw new Error('Erreur inconnue lors de la connexion')
      }
    }
  }


  const logoutUser = () => {
    localStorage.removeItem('token')
    token.value = ''
    axios.defaults.headers.common['Authorization'] = ''
  }
  return {
    token,
    isAuthenticated,
    signup,
    loginUser,
    logoutUser
  }
}
