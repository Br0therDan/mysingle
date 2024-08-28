export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export type Database = {
  public: {
    Tables: {
      accounts: {
        Row: {
          account_name: string
          account_type: Database["public"]["Enums"]["account_type"]
          country_id: number | null
          created_at: string
          id: string
          number_of_employee: number | null
          parent_account_id: string | null
          profile_id: string | null
          segment: Database["public"]["Enums"]["account_segment"] | null
          total_acv: number | null
          updated_at: string
        }
        Insert: {
          account_name: string
          account_type?: Database["public"]["Enums"]["account_type"]
          country_id?: number | null
          created_at?: string
          id?: string
          number_of_employee?: number | null
          parent_account_id?: string | null
          profile_id?: string | null
          segment?: Database["public"]["Enums"]["account_segment"] | null
          total_acv?: number | null
          updated_at?: string
        }
        Update: {
          account_name?: string
          account_type?: Database["public"]["Enums"]["account_type"]
          country_id?: number | null
          created_at?: string
          id?: string
          number_of_employee?: number | null
          parent_account_id?: string | null
          profile_id?: string | null
          segment?: Database["public"]["Enums"]["account_segment"] | null
          total_acv?: number | null
          updated_at?: string
        }
        Relationships: []
      }
      alembic_version: {
        Row: {
          version_num: string
        }
        Insert: {
          version_num: string
        }
        Update: {
          version_num?: string
        }
        Relationships: []
      }
      contacts: {
        Row: {
          account_id: string | null
          address: string | null
          business_phone: string | null
          created_at: string
          email: string | null
          first_name: string | null
          full_name: string | null
          id: string
          job_role: string | null
          job_type: string | null
          jop_level: string | null
          last_name: string | null
          mobile_phone: string | null
          profile_id: string | null
          relationship_strength: string | null
          reporting_manager: string | null
        }
        Insert: {
          account_id?: string | null
          address?: string | null
          business_phone?: string | null
          created_at?: string
          email?: string | null
          first_name?: string | null
          full_name?: string | null
          id?: string
          job_role?: string | null
          job_type?: string | null
          jop_level?: string | null
          last_name?: string | null
          mobile_phone?: string | null
          profile_id?: string | null
          relationship_strength?: string | null
          reporting_manager?: string | null
        }
        Update: {
          account_id?: string | null
          address?: string | null
          business_phone?: string | null
          created_at?: string
          email?: string | null
          first_name?: string | null
          full_name?: string | null
          id?: string
          job_role?: string | null
          job_type?: string | null
          jop_level?: string | null
          last_name?: string | null
          mobile_phone?: string | null
          profile_id?: string | null
          relationship_strength?: string | null
          reporting_manager?: string | null
        }
        Relationships: []
      }
      contacts_opportunities: {
        Row: {
          contact_id: string
          is_primary: boolean | null
          opportunity_id: string
        }
        Insert: {
          contact_id: string
          is_primary?: boolean | null
          opportunity_id: string
        }
        Update: {
          contact_id?: string
          is_primary?: boolean | null
          opportunity_id?: string
        }
        Relationships: []
      }
      daily_scrums: {
        Row: {
          id: string
          project_id: string
          scrum_date: string
          sprint_id: string
          summary: string | null
        }
        Insert: {
          id?: string
          project_id: string
          scrum_date: string
          sprint_id: string
          summary?: string | null
        }
        Update: {
          id?: string
          project_id?: string
          scrum_date?: string
          sprint_id?: string
          summary?: string | null
        }
        Relationships: []
      }
      opportunities: {
        Row: {
          account_id: string
          close_date: string
          created_at: string
          currency_code: string
          forecast_category: Database["public"]["Enums"]["forcast_category"]
          id: string
          net_new_acv: number
          opportunity_contact: string | null
          opportunity_name: string
          opportunity_summary: string | null
          opportunity_type:
            | Database["public"]["Enums"]["opportunity_type"]
            | null
          partner: string | null
          profile_id: string
          stage: Database["public"]["Enums"]["opportunity_stage"]
          updated_at: string
        }
        Insert: {
          account_id: string
          close_date: string
          created_at?: string
          currency_code: string
          forecast_category?: Database["public"]["Enums"]["forcast_category"]
          id?: string
          net_new_acv: number
          opportunity_contact?: string | null
          opportunity_name: string
          opportunity_summary?: string | null
          opportunity_type?:
            | Database["public"]["Enums"]["opportunity_type"]
            | null
          partner?: string | null
          profile_id: string
          stage?: Database["public"]["Enums"]["opportunity_stage"]
          updated_at?: string
        }
        Update: {
          account_id?: string
          close_date?: string
          created_at?: string
          currency_code?: string
          forecast_category?: Database["public"]["Enums"]["forcast_category"]
          id?: string
          net_new_acv?: number
          opportunity_contact?: string | null
          opportunity_name?: string
          opportunity_summary?: string | null
          opportunity_type?:
            | Database["public"]["Enums"]["opportunity_type"]
            | null
          partner?: string | null
          profile_id?: string
          stage?: Database["public"]["Enums"]["opportunity_stage"]
          updated_at?: string
        }
        Relationships: []
      }
      "opportunities-accounts": {
        Row: {
          account_id: string
          created_at: string
          is_partner: boolean | null
          is_primary_partner: boolean | null
          opportunity_id: string
        }
        Insert: {
          account_id: string
          created_at?: string
          is_partner?: boolean | null
          is_primary_partner?: boolean | null
          opportunity_id: string
        }
        Update: {
          account_id?: string
          created_at?: string
          is_partner?: boolean | null
          is_primary_partner?: boolean | null
          opportunity_id?: string
        }
        Relationships: []
      }
      organizations: {
        Row: {
          created_at: string
          id: string
          org_name: string | null
          org_type: Database["public"]["Enums"]["org_type"]
          updated_at: string
        }
        Insert: {
          created_at?: string
          id?: string
          org_name?: string | null
          org_type: Database["public"]["Enums"]["org_type"]
          updated_at?: string
        }
        Update: {
          created_at?: string
          id?: string
          org_name?: string | null
          org_type?: Database["public"]["Enums"]["org_type"]
          updated_at?: string
        }
        Relationships: []
      }
      profiles: {
        Row: {
          avatar_url: string | null
          created_at: string
          email: string
          first_name: string | null
          full_name: string | null
          id: string
          is_verified: boolean
          job_role: string | null
          last_name: string | null
          org_id: string | null
          updated_at: string
          username: string | null
          website: string | null
          work_email: string | null
        }
        Insert: {
          avatar_url?: string | null
          created_at?: string
          email: string
          first_name?: string | null
          full_name?: string | null
          id: string
          is_verified?: boolean
          job_role?: string | null
          last_name?: string | null
          org_id?: string | null
          updated_at?: string
          username?: string | null
          website?: string | null
          work_email?: string | null
        }
        Update: {
          avatar_url?: string | null
          created_at?: string
          email?: string
          first_name?: string | null
          full_name?: string | null
          id?: string
          is_verified?: boolean
          job_role?: string | null
          last_name?: string | null
          org_id?: string | null
          updated_at?: string
          username?: string | null
          website?: string | null
          work_email?: string | null
        }
        Relationships: [
          {
            foreignKeyName: "profiles_id_fkey"
            columns: ["id"]
            isOneToOne: true
            referencedRelation: "users"
            referencedColumns: ["id"]
          },
        ]
      }
      profiles_projects: {
        Row: {
          joined_at: string
          profile_id: string
          project_id: string
          role: string | null
        }
        Insert: {
          joined_at?: string
          profile_id: string
          project_id: string
          role?: string | null
        }
        Update: {
          joined_at?: string
          profile_id?: string
          project_id?: string
          role?: string | null
        }
        Relationships: []
      }
      projects: {
        Row: {
          account_id: string
          created_at: string
          description: string | null
          id: string
          opportunity_id: string | null
          profile_id: string
          project_name: string
          updated_at: string
        }
        Insert: {
          account_id: string
          created_at?: string
          description?: string | null
          id?: string
          opportunity_id?: string | null
          profile_id: string
          project_name: string
          updated_at?: string
        }
        Update: {
          account_id?: string
          created_at?: string
          description?: string | null
          id?: string
          opportunity_id?: string | null
          profile_id?: string
          project_name?: string
          updated_at?: string
        }
        Relationships: []
      }
      sprints: {
        Row: {
          capacity: number | null
          created_at: string
          end_date: string
          goal: string | null
          id: string
          project_id: string
          retrospective: string | null
          sprint_name: string
          start_date: string
          status: Database["public"]["Enums"]["status"]
          updated_at: string
          velocity: number | null
        }
        Insert: {
          capacity?: number | null
          created_at?: string
          end_date: string
          goal?: string | null
          id?: string
          project_id: string
          retrospective?: string | null
          sprint_name: string
          start_date: string
          status?: Database["public"]["Enums"]["status"]
          updated_at?: string
          velocity?: number | null
        }
        Update: {
          capacity?: number | null
          created_at?: string
          end_date?: string
          goal?: string | null
          id?: string
          project_id?: string
          retrospective?: string | null
          sprint_name?: string
          start_date?: string
          status?: Database["public"]["Enums"]["status"]
          updated_at?: string
          velocity?: number | null
        }
        Relationships: []
      }
      tasks: {
        Row: {
          actual_time: number | null
          assigned_to: string
          created_at: string
          description: string | null
          due_date: string
          estimated_time: number | null
          id: string
          priority: string
          related_task_id: string | null
          sprint_id: string
          status: Database["public"]["Enums"]["status"]
          task_name: string
          updated_at: string
        }
        Insert: {
          actual_time?: number | null
          assigned_to: string
          created_at?: string
          description?: string | null
          due_date: string
          estimated_time?: number | null
          id?: string
          priority?: string
          related_task_id?: string | null
          sprint_id: string
          status: Database["public"]["Enums"]["status"]
          task_name: string
          updated_at?: string
        }
        Update: {
          actual_time?: number | null
          assigned_to?: string
          created_at?: string
          description?: string | null
          due_date?: string
          estimated_time?: number | null
          id?: string
          priority?: string
          related_task_id?: string | null
          sprint_id?: string
          status?: Database["public"]["Enums"]["status"]
          task_name?: string
          updated_at?: string
        }
        Relationships: []
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      account_segment:
        | "ENTERPRISE"
        | "CORPORATE"
        | "SMB"
        | "STARTUP"
        | "GOVERNMENT"
        | "NON PROFIT"
      account_type: "PROSPECT" | "CUSTOMER" | "PARTNER" | "INACTIVE"
      forcast_category: "PIPELINE" | "UPSIDE" | "EXPECT" | "COMMIT" | "CLOSED"
      opportunity_stage:
        | "1 _OPPORTUNITY"
        | "2_DISCOVERY"
        | "3_OBJECTIVES"
        | "4_PRESENT_SOLUTION"
        | "4_ECONOMIC_BUYER_IDNETIFIED"
        | "5_ECONOMIC_BUYER_VALIDATION"
        | "6_VALIDATION_COMPLETED"
        | "7_DEAL_IMMINENT"
        | "8_CLOSED_LOST"
        | "8_CLOSED_NO_DECISION"
        | "9_CLOSED_WON"
      opportunity_type: "NEW_BUSINESS" | "UPSELL" | "RENEWAL"
      org_type: "INTERNAL" | "EXTERNAL"
      status:
        | "IN_REVIEW"
        | "PLANNED"
        | "SCHEDULED"
        | "IN_PROGRESS"
        | "COMPLETED"
        | "CANCELLED"
        | "BLOCKED"
        | "ON_HOLD"
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}

type PublicSchema = Database[Extract<keyof Database, "public">]

export type Tables<
  PublicTableNameOrOptions extends
    | keyof (PublicSchema["Tables"] & PublicSchema["Views"])
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof (Database[PublicTableNameOrOptions["schema"]]["Tables"] &
        Database[PublicTableNameOrOptions["schema"]]["Views"])
    : never = never,
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? (Database[PublicTableNameOrOptions["schema"]]["Tables"] &
      Database[PublicTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : PublicTableNameOrOptions extends keyof (PublicSchema["Tables"] &
        PublicSchema["Views"])
    ? (PublicSchema["Tables"] &
        PublicSchema["Views"])[PublicTableNameOrOptions] extends {
        Row: infer R
      }
      ? R
      : never
    : never

export type TablesInsert<
  PublicTableNameOrOptions extends
    | keyof PublicSchema["Tables"]
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? Database[PublicTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : PublicTableNameOrOptions extends keyof PublicSchema["Tables"]
    ? PublicSchema["Tables"][PublicTableNameOrOptions] extends {
        Insert: infer I
      }
      ? I
      : never
    : never

export type TablesUpdate<
  PublicTableNameOrOptions extends
    | keyof PublicSchema["Tables"]
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? Database[PublicTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : PublicTableNameOrOptions extends keyof PublicSchema["Tables"]
    ? PublicSchema["Tables"][PublicTableNameOrOptions] extends {
        Update: infer U
      }
      ? U
      : never
    : never

export type Enums<
  PublicEnumNameOrOptions extends
    | keyof PublicSchema["Enums"]
    | { schema: keyof Database },
  EnumName extends PublicEnumNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicEnumNameOrOptions["schema"]]["Enums"]
    : never = never,
> = PublicEnumNameOrOptions extends { schema: keyof Database }
  ? Database[PublicEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : PublicEnumNameOrOptions extends keyof PublicSchema["Enums"]
    ? PublicSchema["Enums"][PublicEnumNameOrOptions]
    : never
