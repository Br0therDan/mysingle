import { combineReducers } from '@reduxjs/toolkit'
import appReducer from '@/store/reducers/app-reducer'
import sidebarSlice from './slices/sidebarSlice'

// Nested Persists
const rootReducer = combineReducers({
  app: appReducer,
  sidebar: sidebarSlice,
})

export default rootReducer
