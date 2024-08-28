import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const profilesConfig: BaseEntityConfig = {
  identifierKey: 'profile_id',
  fields: {
    full_name: {
      type: 'string',
      label: 'full_name',
      placeholder: 'Enter full name',
      showInForm: true,
      showInTable: true,
    },
    email: {
      type: 'string',
      label: 'email',
      placeholder: 'Enter email',
      showInForm: true,
      showInTable: true,
    },
    job_role: {
      type: 'string',
      label: 'job_role',
      placeholder: 'Enter job role',
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    full_name: z.string().nonempty("Full name is required"),
    email: z.string().email("Invalid email address"),
    job_role: z.string().optional(),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
