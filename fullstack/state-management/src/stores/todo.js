import { defineStore } from 'pinia'

export const useTodoStore = defineStore('todo', {
    state: () => ({
        todos: []
    }),
    getters: {
        totalTodos: (state) => state.todos.length
    },
    actions: {
        addTodo(task) {
            this.todos.push({
                id: Date.now(),
                text: task,
                completed: false
            })
        },
        removeTodo(id) {
            this.todos = this.todos.filter(todo => todo.id !== id)
        },
        toggleTodo(id) {
            const todo = this.todos.find(todo => todo.id === id)
            if (todo) todo.completed = !todo.completed
        }
    }
})