import { setCookie } from '@/lib/utils/cookie'
import { createSlice, PayloadAction } from '@reduxjs/toolkit'


// Define a type for the slice state
interface State {
  theme: string
  layout: number[]
  collapsed: boolean
}

// Define the initial state using that type
const initialState: State = {
  theme: 'system',
  layout: [25, 75],
  collapsed: false,
}

export const slice = createSlice({
  name: 'app',
  initialState,
  reducers: {
    setAppTheme: (state, action: PayloadAction<State['theme']>) => {
      state.theme = action.payload
      setCookie('app:theme', action.payload)
    },
    // setAppLanguage: (state, action: PayloadAction<State['language']>) => {
    //   state.language = action.payload
    //   document.documentElement.lang = action.payload
    //   setCookie('app:language', action.payload)
    // },
    setAppLayout: (state, action: PayloadAction<State['layout']>) => {
      state.layout = action.payload
    },
    setAppCollapsed: (state, action: PayloadAction<State['collapsed']>) => {
      state.collapsed = action.payload
    },
  },
})

export const { setAppTheme, setAppLayout, setAppCollapsed } =
  slice.actions

export default slice.reducer
