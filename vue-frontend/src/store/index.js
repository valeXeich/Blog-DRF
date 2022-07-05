import { createStore } from 'vuex'

export default createStore({
    state: {
        isAuthenticated: false,
        token_access: '',
        token_refresh: '',
        username: '',
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token_access')) {
                state.token_access = localStorage.getItem('token_access')
                state.token_refresh = localStorage.getItem('token_refresh')
                state.username = localStorage.getItem('username')
                state.isAuthenticated = true
            } else {
                state.token_access = ''
                state.token_refresh = ''
                 state.username = ''
                state.isAuthenticated = false
            }
        },
        setToken(state, token_access, token_refresh) {
            state.token_access = token_access
            state.token_refresh = token_refresh
            state.isAuthenticated = true
        },
        removeToken(state) {
            state.token_access = ''
            state.token_refresh = ''
            state.isAuthenticated = false
            state.username = ''
        }
    },
})