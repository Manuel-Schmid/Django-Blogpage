import { defineStore } from 'pinia'

export const useStore = defineStore('main2', {
  state: () =>
    ({
      count: 0,
    }),
  getters: {
    counter: (state) => state.count,
  },
  actions: {
    increment() {
      this.count += 2;
    },
  },
})