from pydantic import BaseModel, Field


class PunishmentStatistics(BaseModel):
    watchdogLastMinute: int = Field(alias="watchdog_lastMinute")
    staffRollingDaily: int = Field(alias="staff_rollingDaily")
    watchdogTotal: int = Field(alias="watchdog_total")
    watchdogRollingDaily: int = Field(alias="watchdog_rollingDaily")
    staffTotal: int = Field(alias="staff_total")
