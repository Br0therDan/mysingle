// src/config/entities/opportunities.ts
import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const opportunitiesConfig: BaseEntityConfig = {
  identifierKey: 'opportunity_id',
  fields: {
    opportunity_name: {
      type: 'string',
      label: 'opportunity_name',
      placeholder: 'Enter opportunity name',
      disabled: (id?: string) => Boolean(id),
      showInForm: true,
      showInTable: true,
    },
    stage: {
      type: 'string',
      label: 'stage',
      placeholder: 'Select stage',
      options: ['Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost'],
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
    ...commonFields,
  },
  schema: z.object({
    opportunity_name: z.string().nonempty("Opportunity name is required"),
    stage: z.enum(['Qualification', 'Proposal', 'Negotiation', 'Closed Won', 'Closed Lost']),
    account_id: z.string().nonempty("Account ID is required"),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
