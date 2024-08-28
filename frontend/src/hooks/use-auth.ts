'use client'

import { AuthContext, AuthContextProps } from '@/context/auth-provider'
import * as React from 'react'

const useAuth = () => {
  const context = React.useContext<AuthContextProps | undefined>(AuthContext)

  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }

  return context
}

export { useAuth }
