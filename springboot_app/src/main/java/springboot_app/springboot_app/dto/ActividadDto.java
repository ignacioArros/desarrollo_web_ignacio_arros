package springboot_app.springboot_app.dto;

import springboot_app.springboot_app.models.ActividadTema;
import java.time.LocalDateTime;
import java.util.List;

public class ActividadDto {
    private Integer id;
    private LocalDateTime diaHoraInicio;
    private String sector;
    private String nombre;
    private List<ActividadTema> temas;
    private String promedioNotas;

    // Getters y setters
    public Integer getId() { 
        return id; 
    }

    public void setId(Integer id) { 
        this.id = id; 
    }

    public LocalDateTime getDiaHoraInicio() { 
        return diaHoraInicio; 
    }

    public void setDiaHoraInicio(LocalDateTime diaHoraInicio) { 
        this.diaHoraInicio = diaHoraInicio; 
    }

    public String getSector() { 
        return sector; 
    }

    public void setSector(String sector) { 
        this.sector = sector; 
    }

    public String getNombre() { 
        return nombre; 
    }

    public void setNombre(String nombre) { 
        this.nombre = nombre; 
    }

    public List<ActividadTema> getTemas() { 
        return temas; 
    }

    public void setTemas(List<ActividadTema> temas) { 
        this.temas = temas; 
    }

    public String getPromedioNotas() { 
        return promedioNotas; 
    }

    public void setPromedioNotas(String promedioNotas) { 
        this.promedioNotas = promedioNotas; 
    }
    
}
