import { createSlice } from '@reduxjs/toolkit'

export interface SidebarState {
  isExpanded: boolean
}

const initialState: SidebarState = {
  isExpanded: false,
}

const sidebarSlice = createSlice({
  name: 'sidebar',
  initialState,
  reducers: {
    toggleSidebar: (state) => {
      state.isExpanded = !state.isExpanded
    },
    expandSidebar: (state) => {
      state.isExpanded = true
    },
    collapseSidebar: (state) => {
      state.isExpanded = false
    },
  },
})

export const { toggleSidebar, expandSidebar, collapseSidebar } =
  sidebarSlice.actions
export default sidebarSlice.reducer
