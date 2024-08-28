import rootReducer from './root-reducer'
import { configureStore } from '@reduxjs/toolkit'

export const store = configureStore({
  reducer: rootReducer,
})

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;