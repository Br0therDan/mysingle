import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const organizationsConfig: BaseEntityConfig = {
  identifierKey: 'org_id',
  fields: {
    org_name: {
      type: 'string',
      label: 'organization_name',
      placeholder: 'Enter organization name',
      disabled: (id?: string) => Boolean(id),
      showInForm: true,
      showInTable: true,
    },
    org_type: {
      type: 'string',
      label: 'organization_type',
      placeholder: 'Select organization type',
      options: ['Corporate', 'Non-Profit', 'Government'],
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    org_name: z.string().nonempty("Organization name is required"),
    org_type: z.enum(['Corporate', 'Non-Profit', 'Government']),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
