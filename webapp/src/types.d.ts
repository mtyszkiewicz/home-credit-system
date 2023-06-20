export interface User {
    id: string;
    name: string;
    image: string;
    score: number;
    color: string;
}

export interface Activity {
    id: number;
    name: string;
    value: number;
    icon: string;
}

export interface ActivityRecord {
    id: number;
    timestamp: string;
    user: User;
    activity: Activity;
    time: string;
}

export interface ActivityRecordsHistory {
    date: string;
    records: ActivityRecord[];
}

export interface ActivityRecordCreate {
    user_id: number;
    activity_id: number;
}

export interface ActivitySummary {
    id: number;
    name: string;
    count: number;
    total_value: number;
    icon: string;
    description: string;
    group_name: string;
}

export interface UserActivitySummary {
    user: User;
    activity_summary: ActivitySummary[];
}