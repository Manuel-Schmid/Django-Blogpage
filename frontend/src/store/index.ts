import { defineStore } from 'pinia'

export const useStore = defineStore('main', {
  state: () =>
    ({
      count: 0,
    }),
  getters: {
    counter: (state) => state.count,
  },
  actions: {
    increment() {
      this.count++
    },
  },
  persist: {
    enabled: true
  }
})