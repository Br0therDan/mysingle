// src/config/entities/index.ts

import { accountsConfig } from './accounts';
import { dailyScrumsConfig } from './dailyScrums';
import { opportunitiesConfig } from './opportunities';
import { organizationsConfig } from './organizations';
import { profilesConfig } from './profiles';
import { projectsConfig } from './projects';
import { sprintsConfig } from './sprints';
import { tasksConfig } from './tasks';
import { BaseEntityConfig } from '@/types/base';

export const entityConfigMap: Record<string, BaseEntityConfig> = {
  accounts: accountsConfig,
  dailyScrums: dailyScrumsConfig,
  opportunities: opportunitiesConfig,
  organizations: organizationsConfig,
  profiles: profilesConfig,
  projects: projectsConfig,
  sprints: sprintsConfig,
  tasks: tasksConfig,
};
