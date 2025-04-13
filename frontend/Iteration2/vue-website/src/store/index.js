import { createStore } from 'vuex'

export default createStore({
  state: {
    species: [],
    selectedSpecies: null
  },
  getters: {
    getSpecies: state => state.species,
    getSelectedSpecies: state => state.selectedSpecies
  },
  mutations: {
    SET_SPECIES(state, species) {
      state.species = species
    },
    SET_SELECTED_SPECIES(state, species) {
      state.selectedSpecies = species
    }
  },
  actions: {
    setSpecies({ commit }, species) {
      commit('SET_SPECIES', species)
    },
    setSelectedSpecies({ commit }, species) {
      commit('SET_SELECTED_SPECIES', species)
    }
  },
  modules: {
  }
}) 