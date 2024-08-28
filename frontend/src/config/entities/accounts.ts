import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const accountsConfig: BaseEntityConfig = {
  identifierKey: 'account_id',
  fields: {
    account_name: {
      type: 'string',
      label: 'account_name',
      placeholder: 'Enter account name',
      disabled: (id?: string) => Boolean(id),
      showInForm: true,
      showInTable: true,
      linkTemplate: '/accounts/{id}', // 링크 템플릿
    },
    account_type: {
      type: 'string',
      label: 'account_type',
      placeholder: 'Select account type',
      options: ['Prospect', 'Customer', 'Partner'],
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    account_name: z.string().nonempty("Account name is required"),
    account_type: z.enum(['Prospect', 'Customer', 'Partner']),
    owner: z.string().optional(),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
