import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios, { AxiosError } from 'axios'

// Création d'un store pour l'authentification
export const useAuth = () => {
  const token = ref(localStorage.getItem('token') || '')
  const isAuthenticated = ref(!!token.value)
  const router = useRouter()
  const setToken = (newToken: string) => {
    token.value = newToken
    isAuthenticated.value = true
    }

  // Fonction de connexion
  const loginUser = async (username: string, password: string) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/login/', {
        username,
        password
      })
      
      // Stockage du token dans le localStorage
      localStorage.setItem('token', response.data.token)
      token.value = response.data.token
      isAuthenticated.value = true
      router.push('/dashboard')

    } catch (error) {
      if (error instanceof AxiosError) {
        alert(error.response?.data.error || 'Erreur lors de la connexion')
      } else {
        alert('Une erreur inconnue est survenue')
      }
    }
  }

  // Fonction d'inscription
  const signup = async (username: string, email: string, password: string) => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/register/', {
        username,
        email,
        password
      })
      
      // Enregistrement du token
      localStorage.setItem('token', response.data.token)
      token.value = response.data.token
      isAuthenticated.value = true
      return true

    } catch (error) {
        if (error instanceof AxiosError) {
          throw new Error(error.response?.data.error || 'Erreur lors de l\'inscription')
        } else {
          throw new Error('Erreur inconnue')
      }
    }
  }

  // Fonction de déconnexion
  const logoutUser = () => {
    localStorage.removeItem('token')
    token.value = ''
    isAuthenticated.value = false
    router.push('/login')
  }

  return {
    token,
    isAuthenticated,
    loginUser,
    signup,
    logoutUser
  }
}
