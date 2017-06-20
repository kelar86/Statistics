package com.gb.statistics.webservice.repository;


import com.gb.statistics.webservice.entity.Site;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;

public interface SiteRepository extends JpaRepository<Site,Long> {

    @Modifying
    Site update(Site site);
 }
