import apiClient from '../api/axios';

class ObjetService {
  getAllObjets() {
    return apiClient.get('/api/v1/objets/');
  }

  getObjet(id) {
    return apiClient.get(`/api/v1/objets/${id}/`);
  }

  createObjet(objet) {
    return apiClient.post('/api/v1/objets/', objet);
  }

  updateObjet(id, objet) {
    return apiClient.put(`/api/v1/objets/${id}/`, objet);
  }

  deleteObjet(id) {
    return apiClient.delete(`/api/v1/objets/${id}/`);
  }
}

export default new ObjetService();