import { z } from 'zod';
import { BaseEntityConfig } from '@/types/base';
import { commonFields } from '@/config/base';

export const dailyScrumsConfig: BaseEntityConfig = {
  identifierKey: 'daily_scrum_id',
  fields: {
    scrum_date: {
      type: 'string',
      label: 'scrum_date',
      placeholder: 'Enter scrum date',
      showInForm: true,
      showInTable: true,
    },
    project_id: {
      type: 'string',
      label: 'project_id',
      placeholder: 'Select project',
      showInForm: true,
      showInTable: false,
    },
    summary: {
      type: 'string',
      label: 'summary',
      placeholder: 'Enter summary',
      showInForm: true,
      showInTable: true,
    },
    ...commonFields,
  },
  schema: z.object({
    scrum_date: z.string().nonempty("Scrum date is required"),
    project_id: z.string().nonempty("Project ID is required"),
    summary: z.string().optional(),
    created_at: z.string().optional(),
    updated_at: z.string().optional(),
  }),
};
