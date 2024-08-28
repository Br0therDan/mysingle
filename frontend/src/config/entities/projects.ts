import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const projectsConfig: BaseEntityConfig = {
  identifierKey: 'project_id',
  fields: {
    project_name: {
      type: 'string',
      label: 'project_name',
      placeholder: 'Enter project name',
      disabled: (id?: string) => Boolean(id),
      showInForm: true,
      showInTable: true,
    },
    account_id: {
      type: 'string',
      label: 'account_id',
      placeholder: 'Select account',
      showInForm: true,
      showInTable: false,
    },
    description: {
      type: 'string',
      label: 'description',
      placeholder: 'Enter description',
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    project_name: z.string().nonempty("Project name is required"),
    account_id: z.string().nonempty("Account ID is required"),
    description: z.string().optional(),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
